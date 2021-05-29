'''
작성일자 : 2021-04-27
작성자 : 이예희
작성내용 : 과제3. 이메일 주소 가져오기

조건 :
- 원본데이터 : 
  https://docs.google.com/spreadsheets/d/1ZhGlXpVRD8Sv5PlkQQl5Usx0di7UB1c47OnwHA4sv5g/edit#gid=2073175037
- open() 사용해서 excel 파일 불러오기
- 이메일 주소의 아이디부분을 슬라이싱을 활용해서 추출
- epass의 아이디와 슬라이싱된 이메일아이디가 다르면, 
  replace를 사용해 epass 아이디를 이메일아이디로 변경
- 변경된 데이터를 pandas를 사용해 excel파일로 저장
- 저장 파일명 : epass.csv OR epass.xlsx
'''