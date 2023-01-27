# Model Loading
### `model.save()`
- 학습의 결과를 저장하기 위한 함수
- 모델 형태(architecture)와 파라메터를 저장
- 모델 학습 중간 과정의 저장을 통해 최선의 결과모델을 선택
- 만들어진 모델을 외부 연구자와 공유하여 학습 재연성 향상

### checkpoints
- 학습의 중간 결과를 저장하여 최선의 결과를 선택하기 위함
- early stopping 기법 사용 시 이전 학습의 결과물을 저장
- loss와 metric 값을 지속적으로 확인 저장
- 일반적으로 epoch, loss, metric을 함께 저장하여 확인

### transfer learning
- 다른 데이터셋으로 만든 모델을 현재 데이터에 적용
- 일반적으로 대용량 데이터셋으로 만들어진 모델의 성능이 높음
- 현재의 DL에서는 가장 일반적인 학습 기법
- backbone architecture가 잘 학습된 모델에서 일부분만 변경하여 학습을 수행함

### freezing
- pretrained model을 활용 시 모델의 일부분을 frozen 시킴
- gradient의 update가 되지 못하도록 하는 것을 의미함