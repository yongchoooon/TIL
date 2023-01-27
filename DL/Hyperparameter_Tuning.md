# Hyperparameter Tuning
> 딥러닝에서 학습의 성능을 높이는 데에는 모델의 영향이 크지만, 현재에는 좋은 모델들이 이미 많이 나와있고 일반화가 되어있다. 그 다음으로는 데이터를 최대한 많이 학습시키는 것인데, 이는 여러 가지 이유로 불가능한 경우도 많다. 그 다음으로 성능을 높이기 위한 방법이 Hyperparameter Tuning인데, 이를 통해서 얻을 수 있는 유익은 그렇게 크지는 않다. 하지만 최후의 방법으로서 시도해 볼 만한 방법이다.
- 모델 스스로 학습하지 않는 값으로, 사람이 지정해준다. (learning rate, 모델의 크기, optimizer 등)
- hyperparameter에 의해 값이 크게 좌우되는 경우도 있긴 하다.
- 마지막 0.01을 쥐어짜야 할 때 도전해볼 만 하다.
- 가장 기본적인 방법 : Grid Search, Random Search
- 최근에는 **베이지안 기반 기법**들이 주도적임

### Ray
- multi-node multi processing 지원 모듈
- ML/DL의 병렬 처리를 위해 개발된 모듈
- 기본적으로 현재의 분산병렬 ML/DL 모듈의 표준
- **Hyperparameter Search를 위한 다양한 모듈 제공**