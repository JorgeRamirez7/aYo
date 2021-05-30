from azure.get_query import GetQuery
from skills.introduction_skill import IntroductionSkill

ayo_introduction = True

def main():
    if ayo_introduction:
        IntroductionSkill().ayo_intro()
    GetQuery().get_query()

if __name__ == "__main__":
    main()
