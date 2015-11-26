import xml.etree.ElementTree as ET
tree = ET.parse("breakfast_menu.xml")
root = tree.getroot()

import HTML

t = HTML.Table(header_row=["Name", "Price", "Description", "Calories"])

for food in root:
        name = food.find('name').text
        price = food.find('price').text
        description = food.find('description').text
        calories = food.find('calories').text
        
        if int(calories) > 700:
                t.rows.append([name, price, description, calories])

        if float(price[1:]) > 8:
                t.rows.append([HTML.TableCell(name, bgcolor='red'),
                               HTML.TableCell(price, bgcolor='red'),
                               HTML.TableCell(description, bgcolor='red'),
                               HTML.TableCell(calories, bgcolor='red')])

html_code = str(t)

html_file= open("test.html", "w")
html_file.write(html_code)
html_file.close()
