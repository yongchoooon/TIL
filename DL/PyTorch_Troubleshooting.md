# Pytorch Troubleshooting
### OOM(Out fo Memory)이 해결하기 어려운 이유들
- 왜 발생했는지 알기 어려움
- 어디서 발생했는지 알기 어려움
- Error backtracking이 이상한 곳으로 감
- 메모리의 이전 상황의 파악이 어려움
- 그래서 Batch size를 줄여서 GPU clean을 하는 것이 일반적인 방법.
  - 이 이외에도 다양한 문제와 방법이 있다.

### `GPUUtil` 사용하기
- `nvidia-smi`처럼 GPU의 상태를 보여주는 모듈
- iter마다 메모리가 늘어나는지 확인할 수 있다.
```python
!pip install GPUtil

import GPUtil
GPUtil.showUtilization()
```

### `torch.cuda.empty_cache()` 써보기
- 사용되지 않는 GPU상 cache를 정리
- 가용 메모리를 확보
- del과는 구분이 필요하다.
- reset 대신 쓰기 좋은 함수
- loop을 돌기 전에 사용하는 것을 권장

### training loop에 tensor로 축적되는 변수는 확인할 것
- tensor로 처리된 변수는 GPU 상에 메모리 사용
- 해당 변수 loop 안에 연산에 있을 때 GPU에 computational graph를 생성(메모리 잠식)
- 1-d tensor의 경우 python 기본 객체로 만들어줌
  - `.items()` or `float()`

### `del` 명령어를 적절히 사용하기
- 필요가 없어진 변수는 적절히 삭제가 필요함
- python의 메모리 배치 특성상 loop이 끝나도 메모리를 차지함

### 가능한 batch 사이즈 실험해보기
- 학습 시 OOM이 발생했다면 batch 사이즈를 1로 해서 실험해보기

### `torch.no_grad()` 사용하기
- inference 시점에서는 `torch.no_grad()` 구문을 사용
- backward pass로 인해 쌓이는 메모리에서 자유로움 (메모리 buffer 현상에서 자유로움)

### 예상치 못한 에러 메세지
- OOM 말고도 유사한 에러들이 발생
- CUDNN_STATUS_NOT_INIT 이나 device-side-assert 등
- 해당 에러도 cuda와 관련하여 OOM의 일종으로 생각될 수 있으며, 적절한 코드 처리가 필요함

### 그 외에도..
- CNN의 대부분의 에러는 크기가 안 맞아서 생기는 경우 (torchsummary 등으로 사이즈를 맞출 것)
- tensor의 float precicsion을 16bit로 줄일 수도 있음 (그렇게 많이 사용하지는 않음)