# #Ex1
# def fuctionp_t(a,b,c,d):
#     print(a,b,c,d,)
# fuctionp_t("harry",'mayur',"raja",'kala')

# #ex2
def fucti2(narmal,*args):        # narmal statement is always before args fuction see this
    print(narmal)
    for value in args:
        print(value)
    #print(args)
mayur = ("harry", 'mayur', "raja", 'kala',"haa","fe")  # Easy to add any item in list or in tuple
narmal = "This people"
fucti2(narmal,*mayur)
