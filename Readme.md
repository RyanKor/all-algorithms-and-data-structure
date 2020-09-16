# JS Algorithms and Data Structure Class

## 한 줄 강의 평가

- Udemy에서 수강해본 강의 중 프로그래밍 강의와 관련해서는 인생강의가 아닌가 싶다.

## 학습 유의사항

- 수강생에게 어떻게 알고리즘과 자료구조를 실무에서 활용할 수 있게 지도할 수 있을 것인가?

- 실무에서 많이 활용하는 알고리즘은 무엇이 있는가?

- SQL에서 활용하는 B-Tree 사용은 어떻게 지도할 것인가?

## JS 알고리즘, 자료구조 풀이 및 수강생 지도하기(2020.07.07)

- 자바스크립트로 알고리즘 짜려고 보니, 자바스크립트 고유 문법을 활용할 일이 좀 있다보니 애먹는 것 같다.

- `Colt Steele` 이 사람 알고리즘 해설 및 풀이는 내가 기존에 접근하려고 했던 풀이법 / 그리고 Hackerrank와 BOJ 등 고수들의 코드만을 보며 풀이를 추측했던 것들을 옆에서 해설해주는 느낌이라 공부해볼만 한 것 같다.

- 결국은 언어만 다를 뿐, 풀어야하는 문제의 본질에 다가가는 방법은 동일하다.

- Udemy에서 구매한 강의들 중 제일 잘 산 강의가 아닐까 싶다.

## Problem and Solving Problem

- [PPT Slide](https://cs.slides.com/colt_steele/problem-solving-patterns)
- 크게 3가지 문제 풀이 해법으로 접근한다.

  ```
  PROBLEM SOLVING (문제를 풀어가는 과정은 크게 5가지 절차를 밟는다.)
  - Understand the Problem
  - Explore Concrete Examples
  - Break It Down
  - Solve/Simplify
  - Look Back and Refactor
  ```

  ```
  UNDERSTAND THE PROBLEM (문제점 이해하기)
    - Can I restate the problem in my own words?
    - What are the inputs that go into the problem?
    - What are the outputs that should come from the solution to the problem?
    - Can the outputs be determined from the inputs? In other words, do I have enough information to solve the problem? (You may not be able to answer this question until you set about solving the problem. That's okay; it's still worth considering the question at this early stage.)
    - How should I label the important pieces of data that are a part of the problem?
  ```

  ```
  REFACTORING QUESTIONS
    - Can you check the result?
    - Can you derive the result differently?
    - Can you understand it at a glance?
    - Can you use the result or method for some other problem?
    - Can you improve the performance of your solution?
    - Can you think of other ways to refactor?
    - How have other people solved this problem?
  ```

1. `Frequency Count` (`Object`를 사용하는 방법)

- Javascript 객체를 사용해서 문자열에서 단어 또는 숫자의 갯수를 Counting하는 방법 (일종의 파이썬 딕셔너리처럼)

- 객체를 활용할 때, 특히 주의깊게 봐야하는 점이 몇 개 있는데, Naive 해결책과 Refactoring 해결책이 완전히 다른 솔루션이라는 점이다.

- 당연히 Refactoring 되어 있는 솔루션이 모범 정답에 가까운데, Naive Solution을 어떻게 내가 변경할 수 있는지를 더 골똘히 생각해봐야겠다.

  ```
  This pattern uses objects or sets to collect values/frequencies of values

  This can often avoid the need for nested loops or O(N^2) operations with arrays / strings
  ```

2. `Multiple Pointers`를 사용하는 방법

- 어떤 언어를 사용하던 반드시 등장하는 방법이지만, Pointer를 사용해서 문제를 푸는 방법을 안내한다.

- Pointer를 일반적으로 하나만 사용하는 경우는 없고, 좌우 서칭, 증감하는 값의 비교 등에서 활용되서 상당히 유용한 방법으로 언급된다.

  ```
  Creating pointers or values that correspond to an index or position and move towards the beginning, end or middle based on a certain condition

  Very efficient for solving problems with minimal space complexity as well
  ```

3. `Sliding Window Pattern`

- 이 파트에서 예시로 나오는 문제가 MaxSubArraySum인데, 배열의 부분을 나눠서 문제를 풀어보는 방법이다.

- MaxSubArraySum, MinSubArraySum 등에 대한 문제는 사실 빈번하게 등장하는 알고리즘 문제고, 많이 활용된다.

- 그런데 이 문제가 알고리즘 풀이의 기초로 활용된다는 점을 잘 몰랐다.

  ```
  This parttern involves creating a window which can either be an array or number from one position to another.

  Depending on a certain condition, the window either increases or closes (and a new window is created)

  Very useful for keeping track of a subset of data in an array/string etc.
  ```

4. `Divide And Conquer`

- Introduction to Algorithms 라는 책에서 앞부분에 언급이 되어 있어서 종종 봤던 부분이긴한데, 책으로 볼때와 설명을 들을 때랑은 사뭇 느낌이 다르다.

- Colt Steel의 강의에서 가장 좋은 부분은 사람들이 가장 쉽게 접근하는 코딩 방법 (Naive Solution)과 그걸 연산속도를 감안한 모범 답안으로 바꿔서 풀이를 설명해주는 부분인 것 같다.

- 결국 강의의 요점은 충분히 많은 생각을 해보고, 풀이법을 다각도로 생각해봐야한다는 점이다.

  ```
  This pattern involves dividing a data set into smaller chunks
  and then repeating a process with a subset of data.

  This pattern can tremendously decrease time complexity
  ```
