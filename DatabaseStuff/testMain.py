from aYoDatabase import DataBase
from SkillWeather import weather
#theDatabase = DataBase()
#check = theDatabase.CheckLogIn("TimTest1", "84321Green")
#print (check)

#theDatabase.AddUser("aKidd", "coolbeans7")

#print (theDatabase.CreateUserProfile("CoolioMcDoogle", "teryakiGuy7"))
#print (theDatabase.CreateUserProfile("CoolioMcDoogle", "teryakiGuy7"))


skill = weather()
check = skill.getCurrentWeather("London")
print (check)
