from bs4 import BeautifulSoup

html = '''
 <li class="section-process-list__list-item makeThisMove"><div class="section-process-list__item"><div class="section-process-list__title">Discovery</div><div class="section-process-list__content"><ul> <li>Analyze requirements</li> <li>Make high-level estimation</li> <li>Provide technology consulting</li> <li>Exploratory data analysis</li></ul></div></div> </li> <li class="section-process-list__list-item makeThisMove"><div class="section-process-list__item"><div class="section-process-list__title">Project Setup</div><div class="section-process-list__content"><ul> <li>Select the engagement model</li> <li>Build the core team</li> <li>Prepare a roadmap for the project</li> <li>Prepare tech documents</li></ul></div></div> </li> <li class="section-process-list__list-item"><div class="section-process-list__item"><div class="section-process-list__title">Development</div><div class="section-process-list__content"><ul> <li>Use Agile development methodology</li> <li>Progress reporting on each iteration</li> <li>Perform internal and release testing</li></ul></div></div> </li> <li class="section-process-list__list-item"><div class="section-process-list__item"><div class="section-process-list__title">Live Release</div><div class="section-process-list__content"><ul> <li>Final testing of the complete system</li> <li>Solve possible issues</li> <li>Live release after approval</li> <li>Collect feedback</li></ul></div></div> </li> <li class="section-process-list__list-item"><div class="section-process-list__item"><div class="section-process-list__title">Support</div><div class="section-process-list__content"><ul> <li>Knowledge transfer</li> <li>Perform continuous server monitoring</li> <li>Allocate team members to fix bugs and make improvements</li></ul></div></div> </li>
'''

soup = BeautifulSoup(html, 'html.parser')

elems = soup.find_all("li", {"class": "section-process-list__list-item"})

def get_child_tasks(elem):
    inner_div = elem.find('div', {'class': 'section-process-list__content'})
    return [x.text for x in inner_div.find_all('li')]

print([{"title": elem.find("div", {"class": "section-process-list__title"}).text, "tasks": get_child_tasks(elem)} for elem in elems])

