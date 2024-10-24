from bs4 import BeautifulSoup

with open ('home.html', 'r') as html_file:
    content = html_file.read()
    #print(content)
    soup = BeautifulSoup(content, 'lxml')
    #print(soup.prettify())
    courses_html_tags = soup.find_all('h5')
    #print(courses_html_tags)
    #for course in courses_html_tags:
        #print(course.text)

    courses_cards = soup.find_all('div', class_='card')
    for course in courses_cards:
        course_name=course.h5.text
        course_price=course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}')