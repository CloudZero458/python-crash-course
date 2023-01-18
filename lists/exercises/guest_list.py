#guest list
guest_list = ["God", "Malcolm X", "Martin Luther King"]

invite1 = f"Hello {guest_list[0]}, you are invited to my dinner"
invite2 = f"Hello {guest_list[1]}, you are invited to my dinner"
invite3 = f"Hello {guest_list[2]}, you are invited to my dinner"



print(f"{' '.join(guest_list)} \n")

guests_who_cant_attend = f"{guest_list[0]} can\'t make it. \n"
print(guests_who_cant_attend)

guest_list[0] = "Ryan Reynolds"
print(f"{guest_list[0]} will replace him. \n")

print(f"{' '.join(guest_list)} \n")


guest_list.insert(0, "Lucifer" )
guest_list.insert(2,"Bruce Lee")
guest_list.insert(3,"Jackie Chan")
guest_list.append("Nagano")

invite4 = f"Hello {guest_list[3]}, you are invited to my dinner"
invite5 = f"Hello {guest_list[4]}, you are invited to my dinner"
invite6 = f"Hello {guest_list[5]}, you are invited to my dinner"
invite7 = f"Hello {guest_list[6]}, you are invited to my dinner"
invite = print(f"{invite1} \n{invite2} \n{invite3} \n{invite4} \n{invite5} \n{invite6} \n{invite7} \n")

print(f"{' '.join(guest_list)} \n")

cancel_message = print("I can only invite 2 people for dinner")
cancel_invite = print(f"sorry {guest_list.pop(6)} I can't invite you to dinner")
cancel_invite = print(f"sorry {guest_list.pop(5)} I can't invite you to dinner")
cancel_invite = print(f"sorry {guest_list.pop(4)} I can't invite you to dinner")
cancel_invite = print(f"sorry {guest_list.pop(3)} I can't invite you to dinner")
cancel_invite = print(f"sorry {guest_list.pop(2)} I can't invite you to dinner")

print(f"{guest_list[0]} and {guest_list[1]} you are still invited")

del guest_list[0:2]

print("Dinner hsa been cancelled")
print(guest_list)
