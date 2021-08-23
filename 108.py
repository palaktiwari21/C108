import random
import plotly.express as px
import plotly.figure_factory as ff
dice_result=[]
#count=[]
for i in range(0,100):

    dice1=random.randint(1,6)
    print(dice1)
    dice2=random.randint(1,6)
    print(dice2)
    dice_result.append(dice1+dice2)
   # count.append(i)
#ig=px.bar(x=dice_result,y=count)
fig=ff.create_distplot([dice_result],['Result'])
fig.show()