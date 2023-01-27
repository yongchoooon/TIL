# Multi GPU
### 개념 정리
- Node : 시스템 (or 컴퓨터)
  - Single Node Single GPU
  - Single Node Multi GPU
  - Multi Node Multi GPU

### Model parallel
- 다중 GPU에 학습을 분산하는 두 가지 방법
  - 모델을 나누기 / 데이터를 나누기
- 모델을 나누는 것은 생각보다 예전부터 썼음 (AlexNet)
- 모델의 병목, 파이프라인의 어려움 등으로 인해 모델 병렬화는 고난이도 과제
- `.to('cuda:0')`, `.to('cuda:1')`

### Data parallel
- 데이터를 나눠 GPU에 할당 후 결과의 평균을 취하는 방법
- minibatch 수식과 유사한데, 한 번에 여러 GPU에서 수행
- Pytorch에서는 아래 두 가지 방식을 제공
  - `DataParallel` : 단순히 데이터를 분배한 후 평균을 취함
    - -> GPU 사용 불균형 문제 발생, Batch 사이즈 감소 (한 GPU가 병목)
  - `DistributedDataParallel` : 각 CPU마다 process를 생성하여 개별 GPU에 할당
    - -> 기본적으로 `DataParallel`로 하나 개별적으로 연산의 평균을 냄
- Example Code of `DataParallel`
```Python
parallel_model = torch.nn.DataParallel(model) # Encapsulate the model

predictions = parallel_model(inputs)      # Forward pass on multi-GPUs
loss = loss_function(predictions, labels) # Compute loss function
loss.mean().backward()                    # Average GPU-losses + backward pass
optimizer.step()                          # Optimizer stpe
predictions = parallel_model(inputs)      # Forward pass with new parameters
```
