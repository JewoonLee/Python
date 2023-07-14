def std_weight(height,gender):
    h=height/100
    if gender =="여자":
        stdh=h*h*21
    elif gender == "남자":
        stdh=h*h*22
        
    stdh=round(stdh,2)
    
    print("키 "+str(height)+"cm" + gender +"의 표준 체중은 "+str(stdh)+"kg 입니다.")
    return stdh

std_weight(175,"남자")