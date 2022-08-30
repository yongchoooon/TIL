from fastapi import FastAPI
from enum import Enum
import uvicorn
import requests
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings(action='ignore')

app = FastAPI()

# 1.
# {
# "under_1month": 10,
# "3m_to_6m" : 30,
#  "6m_to_1y": 20
#}
# json -> visualization
def make_dataframe(url, serviceKey, pageNo, numOfRows, resultType='json'):
  params ={'serviceKey' : serviceKey, 'pageNo' : pageNo, 'numOfRows' : numOfRows, 'resultType' : resultType}
  response = requests.get(url, params=params)
  data = response.content.decode()

  data_title = url.split('/')[-1]
  return pd.DataFrame(pd.read_json(data)[data_title]['body']['items']['item'])

# 상권 변화 지표
def get_data_ci():
    url = 'http://apis.data.go.kr/6260000/BusanCommercialChangeService/getCommercialChangeList'
    serviceKey = 'sDfk9Qyuq5+oRZaD0XyZ+Zohtbmixn0X3VlBiZHMQAM5OBCSCn+ZTvqoiWBPXS+tZy4mMtWkIUnS6XSpfgJm2w=='
    pageNo = '1'
    numOfRows = '447' # total : 447 rows
    resultType = 'json'

    # Change Indicator
    temp_df_ci =  make_dataframe(url, serviceKey, pageNo, numOfRows, resultType)

    columns = {'type_nm' : '상권_변화_지표_명',
               'comm_nm' : '상권_코드_명',
               'change_indicator_nm' : '상권_구분_코드_명',
               'average_open_months' : '운영_영업_개월_평균',
               'average_close_months' : '폐업_영업_개월_평균',
               'busan_average_open_months' : '부산_운영_영업_개월_평균',
               'busan_average_close_months' : '부산_폐업_영업_개월_평균'}

    return temp_df_ci.rename(columns = columns)

# 상권 변화 지표2 (지역구 column이 추가된 csv 파일 불러오기)
def get_data_ci_2():
    return pd.read_csv('./data/부산광역시_상권_변화지표정보_지역구.csv')

# 상권 집객 시설
def get_data_af():
    url = 'http://apis.data.go.kr/6260000/BusanCommercialCountingService/getCommercialCountingList'
    serviceKey = 'sDfk9Qyuq5+oRZaD0XyZ+Zohtbmixn0X3VlBiZHMQAM5OBCSCn+ZTvqoiWBPXS+tZy4mMtWkIUnS6XSpfgJm2w=='
    pageNo = '1'
    numOfRows = '384' # total : 384 rows
    resultType = 'json'

    # Change Indicator
    temp_df_af =  make_dataframe(url, serviceKey, pageNo, numOfRows, resultType)

    columns = {'type_nm' : '상권_변화_지표_명',
               'comm_nm' : '상권_코드_명',
               'fac_total' : '집객_시설_수',
               'gov_total' : '관공서_수',
               'sch_total' : '학교_시설_수',
               'hos_total' : '병원_시설_수_1',
               'bus_total' : '교통_시설_수',
               'sub_total' : '지하철_수',
               'hot_total' : '병원_시설_수_2',
               'sho_total' : '쇼핑_시설_수'
               }

    return temp_df_af.rename(columns = columns)

# Store History
def get_data_sh():
    url = 'http://apis.data.go.kr/6260000/BusanCommercialHistoryService/getCommercialHistoryList'
    serviceKey = 'sDfk9Qyuq5+oRZaD0XyZ+Zohtbmixn0X3VlBiZHMQAM5OBCSCn+ZTvqoiWBPXS+tZy4mMtWkIUnS6XSpfgJm2w=='
    pageNo = '1'
    numOfRows = '10000' # total : 279096 rows
    resultType = 'json'

    temp_df_sh = make_dataframe(url, serviceKey, pageNo, numOfRows, resultType)

    for i in range(2, 29):
        pageNumber = str(i)
        temp_df_sh = pd.concat([temp_df_sh, make_dataframe(url, serviceKey, pageNo = pageNumber, numOfRows = '10000')], ignore_index = True)

    columns = {'trdstatenm' : '상태_명',
               'bplcnm' : '상점_명',
               'majornm' : '대분류',
               'minornm' : '중분류',
               'upjongnm' : '업종_명(소분류)',
               'rdnwhladdr' : '주소',
               'apvpermymd' : '개업_일',
               'dcbymd' : '폐업_일',
               'geom' : '좌표'}

    return temp_df_sh.rename(columns = columns)


def processing_data_sh(df_sh):
    df_sh["개업_일"][25544] = '1986-02-17'
    df_sh["개업_일"][126926] = '1987-05-13'
    df_sh["개업_일"][271616] = '1987-08-28'

    df_sh["개업_일"][34090] = '1997-01-09'
    df_sh["개업_일"][34091] = '1995-06-02'
    df_sh["개업_일"][52518] = '1996-02-23'
    df_sh["개업_일"][118750] = '1995-11-06'
    df_sh["개업_일"][240395] = '1997-04-16'
    
    df_sh["개업_일"] = pd.to_datetime(df_sh["개업_일"])
    df_sh["폐업_일"] = pd.to_datetime(df_sh["폐업_일"])

    df_sh_address = pd.read_csv("./data/부산광역시_상권_점포이력정보_좌표.csv", encoding = 'cp949')[["지번주소"]]

    df_sh_address["지번주소"][133315] = "부산광역시 강서구 명지동"
    df_sh_address["지번주소"][209329] = "부산광역시 부산진구 초읍동"
    df_sh_address["지번주소"][220485] = "부산광역시 사하구 아미동2가"

    df_sh["지역구"] = df_sh_address["지번주소"].str.split(" ").str[1]
    df_sh["읍면동"] = df_sh_address["지번주소"].str.split(" ").str[2]

    # 점포상태 : 영업/정상, 폐업일 있음 => 폐업으로 처리
    df_sh_temp_index = df_sh[(df_sh["상태_명"] == "영업/정상") & (df_sh["폐업_일"].notnull())].index
    df_sh["상태_명"][df_sh_temp_index] = "폐업"

    # 점포상태 : 폐업, 폐업일 없음 => 삭제
    df_sh_temp_index = df_sh[(df_sh["상태_명"] == "폐업") & (df_sh["폐업_일"].isnull())].index
    df_sh = df_sh.drop(index = df_sh_temp_index, axis = 0)

    # 점포상태 : 취소/말소/만료/정지/중지 - 폐업일 있음 => "폐업"으로 처리
    df_sh_temp_index = df_sh[(df_sh["상태_명"] == "취소/말소/만료/정지/중지") & (df_sh["폐업_일"].notnull())].index
    df_sh["상태_명"][df_sh_temp_index] = "폐업"

    # 점포상태 : 취소/말소/만료/정지/중지 - 폐업일 없음 => 삭제
    df_sh_temp_index = df_sh[(df_sh["상태_명"] == "취소/말소/만료/정지/중지") & (df_sh["폐업_일"].isnull())].index
    df_sh = df_sh.drop(index = df_sh_temp_index, axis = 0)

    # 점포상태 : 휴업 => 삭제
    df_sh_temp_index = df_sh[df_sh["상태_명"] == "휴업"].index
    df_sh = df_sh.drop(index = df_sh_temp_index, axis = 0)

    # 점포상태 : 정상 or 영업중 => "영업/정상"으로 처리
    df_sh_temp_index = df_sh[df_sh["상태_명"].isin(["정상", "영업중"])].index
    df_sh["상태_명"][df_sh_temp_index] = "영업/정상"

    # 점포상태 : "직권말소" => "폐업"으로 처리
    df_sh_temp_index = df_sh[df_sh["상태_명"] == "직권말소"].index
    df_sh["상태_명"][df_sh_temp_index] = "폐업"

    # 점포상태 : "신고취소", "지정취소", "말소" => 삭제
    df_sh_temp_index = df_sh[df_sh["상태_명"].isin(["신고취소", "지정취소", "말소"])].index
    df_sh = df_sh.drop(index = df_sh_temp_index, axis = 0)

    # 점포상태 : NaN (결측치) => 삭제 (폐업으로 추측되지만 폐업일을 알 수 없음)
    df_sh = df_sh.drop(index = 262863, axis = 0)

    # 상태명 : "영업/정상" -> "영업" 치환
    df_sh_temp_index = df_sh[df_sh["상태_명"] == "영업/정상"].index
    df_sh["상태_명"][df_sh_temp_index] = "영업"

    df_sh["영업_운영_기간"] = (pd.datetime.now() - df_sh["개업_일"]).dt.days
    df_sh["폐업_운영_기간"] = (df_sh["폐업_일"] - df_sh["개업_일"]).dt.days
    
    return df_sh

def get_df_status_dong(status, gu, dong, upjong, df_sh):
  temp_df = df_sh[(df_sh["상태_명"] == status) &
                  (df_sh["지역구"] == gu) &
                  (df_sh["읍면동"] == dong) &
                  (df_sh["대분류"] == upjong)]

  return temp_df


def get_df_period_section(status, df):
    period = status + "_운영_기간"
    period_month = status + "_운영_기간(개월)"
    section = status + "_운영_기간_구분"

    temp_df = pd.DataFrame(df[period].map(lambda x : round(x / 30, 1))) #
    temp_df = temp_df.rename(columns = {period : period_month})
    temp_df[section] = np.NaN

    temp_df_u1_index = temp_df[temp_df[period_month] <= 12].index
    temp_df_o1u3_index = temp_df[(temp_df[period_month] > 12) & (temp_df[period_month] <= 36)].index
    temp_df_o3u5_index = temp_df[(temp_df[period_month] > 36) & (temp_df[period_month] <= 60)].index
    temp_df_o5u7_index = temp_df[(temp_df[period_month] > 60) & (temp_df[period_month] <= 72)].index
    temp_df_u7_index = temp_df[temp_df[period_month] > 72].index

    temp_df[section][temp_df_u1_index] = "1년 이하"
    temp_df[section][temp_df_o1u3_index] = "1년 ~ 3년"
    temp_df[section][temp_df_o3u5_index] = "3년 ~ 5년"
    temp_df[section][temp_df_o5u7_index] = "5년 ~ 7년"
    temp_df[section][temp_df_u7_index] = "7년 이상"

    return temp_df


def processing_data_ci_2(df_ci2):
    df_ci_gu = pd.crosstab(
        index = df_ci2.지역구,
        columns = df_ci2.상권_구분_코드_명,
        values = df_ci2.상권_구분_코드_명,
        aggfunc = 'count',
    ).fillna(0).apply(lambda x: x.astype('int64'))
    df_ci_gu = df_ci_gu[['다이나믹', '상권확장', '상권축소', '정체']]

    df_ci_gu = df_ci_gu.reset_index()
    df_ci_gu['상권구분'] = df_ci_gu[df_ci_gu.columns[1:]].apply(lambda x: x.index[x.argmax()], axis = 1)
    df_ci_gu['score'] = df_ci_gu['상권구분'].map({'다이나믹' : 4, '상권확장' : 3, '상권축소' : 2, '정체' : 1})

    df_ci_gu_for_viz = pd.DataFrame(index = df_ci_gu['지역구'], columns = ['상권구분', 'score'], data = df_ci_gu[['상권구분','score']].values)

    return df_ci_gu_for_viz


def processing_data_af(df_af, return_type):
    df_af['병원_시설_수'] = df_af[['병원_시설_수_1', '병원_시설_수_2']].sum(axis = 1)
    df_af_count = df_af[['상권_코드_명', '집객_시설_수', '관공서_수', '학교_시설_수', '병원_시설_수', '교통_시설_수', '쇼핑_시설_수']]
    if (return_type == 'count'):
        return df_af_count
    elif (return_type == 'ratio'):
        df_af_ratio = df_af_count.iloc[:, 2:] / df_af_count.iloc[:, 2:].max(axis = 0)
        df_af_ratio = df_af_ratio.apply(lambda x : round(x * 100, 2))
        df_af_ratio = pd.concat([df_af.iloc[:, :2], df_af_ratio], axis = 1)

        return df_af_ratio

def get_sanggwon(df_af, id):
    name = df_af.iloc[id]['상권_코드_명']
    af = df_af.iloc[id][2:].values.astype(int)
    return name, af

# =====================================================================================================================
# @app.get
# =====================================================================================================================


@app.get("/store-history/running-period")
def get_running_period(gu: str, dong: str, upjong: str):

    df_sh = get_data_sh()

    # processing data
    processed_data = processing_data_sh(df_sh)

    # result data
    df_sh_opened = get_df_status_dong(status = "영업", gu = gu, dong = dong, upjong = upjong, df_sh=processed_data)
    df_sh_opened_section = get_df_period_section(status = "영업", df = df_sh_opened)

    df_opened_for_viz = df_sh_opened_section.groupby(["영업_운영_기간_구분"])["영업_운영_기간(개월)"].count()
    df_opened_for_viz = df_opened_for_viz.reindex(index = ["7년 이상", "5년 ~ 7년", "3년 ~ 5년", "1년 ~ 3년"])

    return df_opened_for_viz.to_dict()

@app.get("/store-history/closure-period")
def get_closure_period(gu: str, dong: str, upjong: str):
    # get data
    # df_ci = get_data_ci()
    # df_af = get_data_af()

    df_sh = get_data_sh()

    # processing data
    processed_data = processing_data_sh(df_sh)

    # result data
    df_sh_closed = get_df_status_dong(status = "폐업", gu = gu, dong = dong, upjong = upjong, df_sh=processed_data)
    df_sh_closed_section = get_df_period_section(status = "폐업", df = df_sh_closed)

    df_closed_for_viz = df_sh_closed_section.groupby(["폐업_운영_기간_구분"])["폐업_운영_기간(개월)"].count()
    df_closed_for_viz = df_closed_for_viz.reindex(index = ["7년 이상", "5년 ~ 7년", "3년 ~ 5년", "1년 ~ 3년"])


    return df_closed_for_viz.to_dict()


@app.get("/change-indicator")
def get_change_indicator():
    df_ci2 = get_data_ci_2()
    df_ci_gu_for_viz = processing_data_ci_2(df_ci2)

    return df_ci_gu_for_viz.to_dict()

#
# # 2.
# # key : 지역 / value: HH/HL/LH/LL
# # {
# # "종로구": "HL" ,
# # "성동구" : "HH"
# #}
# @app.get("/user/{name}")
# def read_user_name(name: str):
#     #code
# 	return {"name": name}

class afReturnType(str, Enum):
    count = "count"
    ratio = "ratio"

@app.get("/attractive-facility")
def get_attractive_facility(id: int, return_type : afReturnType):
    df_af = get_data_af()
    df_af_for_viz = processing_data_af(df_af, return_type)
    sanggwon_name, sanggwon_score = get_sanggwon(df_af_for_viz, id)
    categories = ['관공서', '학교', '병원', '교통', '쇼핑']

    result = dict()
    result["sanggwon_name"] = sanggwon_name
    result["categories"] = categories
    result["sanggwon_score"] = sanggwon_score.tolist()

    return result


if __name__ == "__main__":
	uvicorn.run("main:app")
