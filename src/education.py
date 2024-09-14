class Education:
    def __init__(self,institude:str,degree:str,graduation_year:int,study_field:str):
        self.institude=institude
        self.degree=degree
        self.graduation_year=graduation_year
        self.study_field=study_field

    def __repr__(self):
        return  f'''Education :
            institude:{self.institude} 
            degree:{self.degree}
            graduation_year:{self.graduation_year}
            study_field:{self.study_field}'''
        
    @property
    def institude(self):
      return self.__institude 


    @institude.setter
    def institude(self,value):
        if isinstance(value,str):
            self.__institude = value


    @property
    def degree(self):
        return self.__degree


    @degree.setter
    def degree(self,value):
        if isinstance(value,str):
            self.__degree = value



    @property
    def graduation_year(self):
            return self.__graduation_year


    @graduation_year.setter
    def graduation_year(self,value):
        if isinstance(value,int):
            self.__graduation_year = value    




    @property
    def study_field(self):
        return self.__study_field


    @study_field.setter
    def study_field(self,value):
        if isinstance(value,str):
            self.__study_field = value

if __name__ == "__main__":
    education = Education('S.M Science College','first year',2024,'COMPUTER SCIENCE')
    print(education)    