import turtle
import pandas

screen = turtle.Screen()
screen.title("India States Game")
image = "indiamap_2.gif"
screen.addshape(image)
turtle.shape(image)

l = "Andhra Pradesh, Arunachal Pradesh, Assam, Bihar, Chhattisgarh, Goa, Gujarat, Haryana, Himachal Pradesh, Jharkhand, Karnataka, Kerala, Madhya Pradesh, Maharashtra, Manipur, Meghalaya, Mizoram, Nagaland, Odisha, Punjab, Rajasthan, Sikkim, Tamil Nadu, Telangana, Tripura, Uttar Pradesh,Uttarakhand,West Bengal"

states_list = [i.strip() for i in l.split(",")]
# print(states_list)

# How to get position of mouse cursor on screen
x_coord = []
y_coord = []


def get_mouse_click_coord(x, y):
    print(x, y)
    x_coord.append(x)
    y_coord.append(y)


# for i in states_list:
#     print(i)
turtle.onscreenclick(get_mouse_click_coord)
turtle.mainloop()

print(len(x_coord))


india_states_dict = {
    "states": states_list,
    "x": x_coord,
    "y": y_coord
}

df = pandas.DataFrame(india_states_dict)
df.to_csv("indian_states.csv")
