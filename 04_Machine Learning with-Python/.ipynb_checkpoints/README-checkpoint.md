# Machine Learning

Status: 30-Days-Challenges

# # 1. Introduction

> 머신러닝과 인공지능 관련 책은 많다. 하지만 대부분 컴퓨터 과학을 전공하는 대학원생을 위한 것이고 어려운 수식들로 가득 차있다. 
이는 머신러닝이 연구와 상용 애플리케이션에서 일상적으로 사용되는 방식과 극명하게 대립된다.

저자는 말한다.

요즘에는(집필년도 2016년 기준) 머신러닝을 사용하기 위해 학위를 받을 필요가 없다. 그런데도 복잡한 수학을 동원하지 않고 실용적으로 머신러닝을 구축하는 모든 면을 다루는 책은 매우 드물다. 

미적분, 선형대수, 확률을 공부하지 않았어도 이 책으로 머신러닝을 사용할 수 있게 되기를 바란다.

### 책의 구성

- 1장 - 머신러닝과 머신러닝 애플리케이션의 기초 개념 소개 및 책에서 사용할 환경 설명
- 2장과 3장 - 실전에서 가장 널리 사용하는 머신러닝 알고리즘 설명. 각각의 장단점 논의
- 4장 - 머신러닝에서 데이터 표현 방법이 얼마나 중요한지. 데이터의 어떤 면을 주의 깊게 봐야 하는지.
- 5장 - 모델 평가와 매개변수 튜닝을 위한 고급방법으로 특별히 교차 검증(Cross Validation)과 그리드 서치(Grid Search)에 집중하여 살펴본다.
- 6장 - 모델을 연결하고 워크플로를 캡슐화하는 파이프라인 개념을 설명한다.
- 7장 - 앞 장에서 설명한 방법들을 텍스트 데이터에 적용하는 방법과 텍스트에 특화된 처리기법을 소개
- 8장 - 개괄적인 정리를 하고 좀 더 어려운 주제에 대한 참고 자료를 안내.

### Tip

2장과 3장에서 현장에서 실제로 사용하는 알고리즘을 설명하지만, 초보자가 이 알고리즘을 모두 이해할 필요는 없다.

머신러닝 시스템을 가능한 한 빨리 구축해야 한다면 1장과 중요한 개념을 모두 소개하는 2장의 서두를 읽어보길 바란다. 그런 다음 2장의 '요약 및 정리'로 건너 뛸 수 있다. 여기서 목적에 가장 적합한 모델을 선택하고 그 모델을 자세히 설명한 절을 읽으면 된다. 그런 다음 모델 평가와 튜닝을 위해 5장의 개념을 살펴보면 된다.

- 정리 - to 머신러닝 시스템을 가능한 한 빨리 구축해야 하는 독자에게
    - 1장과 2장의 서두 부분을 읽는다.
    - 2장의 '요약 및 정리'로 빠르게 점프한다
        - 여기서 내가 원하는 목적을 달성할 수 있는 모델을 선택하고
        - 그 모델에 대한 설명 절을 자세하게 읽어본다.
    - 5장으로 가서 모델 평가와 튜닝을 위한 개념을 살펴본다.

### 예제 소스 내려받기

[https://github.com/rickiepark/introduction_to_ml_with_python](https://github.com/rickiepark/introduction_to_ml_with_python)

## contents

- Chap1. 소개
    - Machine Learning, Python, Scikit-Learn
    - 
- Chap2. 지도학습
    - 분류와 회귀
    - 일반화, 과대학접, 과소적합
    - 지도학습 알고리즘
    - 분류 예측의 불확실성 추정
    - 요약 및 정리
- Chap3. 비지도 학습과 데이터 전처리
    - 비지도 학습의 종류
    - 비지도 학습의 도전 과제
    - 데이터 전처리와 스케일 조정
    - 차원 축소, 특성 추출, 매니폴드 학습
    - 군집
    - 요약 및 정리
- Chap4. 데이터 표현과 특성 공학
    - 범주형 변수
    - 구간 분할, 이산화, 선형 모델, 트리 모델
    - 상호작용과 다항식
    - 일변량 비선형 변환
    - 특성 자동 선택
    - 전문가 지식 활용
    - 요약 및 정리
- Chap5. 모델 평가와 성능 향상
    - 교차 검증
    - 그리드 서치
    - 평가 지표와 측정
    - 요약 및 정리
- Chap6. 알고리즘 체인과 파이프 라인
- Chap7. 텍스트 데이터 다루기
- Chap8. 마무리