from azure.get_query import GetQuery
from skills.introduction_skill import IntroductionSkill


def main():
    GetQuery().get_query()

if __name__ == "__main__":
    ayo_introduction = False

    if ayo_introduction:
        IntroductionSkill().ayo_intro()
    main()
