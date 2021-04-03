list = ["A123AA11", "А222АА123", "A12AA123", "A123CC1234", "AA123A12"]
list1 = ["В124ТА28", "АА303УА1254", "У423ТК750","В555РХ39","Н0289КВ28","ММ976ММ777","РМ564ТУ5","У198ТА125"]
list.extend(list1)
list2 = []
import re
for i in range(len(list)):
    list2.append((re.findall(r'[А-Я]{1}\d{3}[А-Я]{2}\d{2,3}', list[i])))
list2 = [x for x in list2 if x]
print(list2)





