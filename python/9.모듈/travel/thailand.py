class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")

# 1-3
if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")

#__main__함수 사용시 : 모듈로 사용할떄는 출력되지 않고 파일 안에서만 출력이 되어 이 모듈이 에러가 발생하진 않는지에 대해 확인가능

