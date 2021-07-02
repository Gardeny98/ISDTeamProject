# ISDTeamProject

### Members
* Kang Yeji(captain) : Presentation, Keyword,Registration, Data Processing, Distribution, Reprot
* Yang Yoonseok : Keyword, Data Visialization, Reprot, Distribution, PPT, Data Processing
* Jeong Jiwon : Distribution, Keyword, Map, Data Processing, Distibution, Database, Report, Data Visialization
* Han Jeongwon : Distribution, Map, Registration, Reprot

#### Link : http://ec2-54-180-88-150.ap-northeast-2.compute.amazonaws.com/

#### Data Source
- http://data.seoul.go.kr/dataList/OA-20279/S/1/datasetView.do
- http://www.gisdeveloper.co.kr/?p=2332

# Infra Structure
![Blank diagram](https://user-images.githubusercontent.com/19159759/124253533-1675db80-db63-11eb-9315-a2f5b171962f.png)
### network Server : Ngnix
### Application Server : AWS EC2
### Database Server : AWS RDS - MySQL

# ERD
![image](https://user-images.githubusercontent.com/19159759/124252270-bdf20e80-db61-11eb-87de-0adf72e91144.png)

# Sequence Diagram
![image](https://user-images.githubusercontent.com/19159759/124252302-c64a4980-db61-11eb-9f93-581dabbd58de.png)

# Home
![HOME](https://user-images.githubusercontent.com/19159759/124250384-cfd2b200-db5f-11eb-813b-e735f75c8e82.png)
### 기능
- 서울시 내 일별 신규 확진자와 누적확진자 수를 보여줍니다.
- 서울시의 확진자의 접촉력(감염 경로) 상위 10곳을 보여줍니다. 
- 지도에서 구별 지도에 마우스를 hover하면 구별 신규 확진자와 누적 확진자를 보여줍니다.
![예시](https://user-images.githubusercontent.com/19159759/124251559-03faa280-db61-11eb-9c01-2864234d9a50.png)



# detail
![detail](https://user-images.githubusercontent.com/19159759/124250312-baf61e80-db5f-11eb-80d1-2dddf149e063.png)
### 기능
- 구별 신규 확진자와 누적 확진자를 보여줍니다.
- 구별 접촉력(감염 경로) 상위 5곳을 파이차트로 보여줍니다.
- 접촉력(감염 경로) 기준 관련도 높은 타 지역구 5곳을 보여줍니다.
- 신규 확진자 수를 바차트로 보여줍니다.
- 누적 확진자 수를 라인차트로 보여줍니다.
