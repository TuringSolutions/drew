from bs4 import BeautifulSoup

html ='''
 <li class="faq-block-list__list-item" itemscope="" itemprop="mainEntity" itemtype="https://schema.org/Question"><div class="faq-btn" id="faq-button-1" aria-expanded="false"> <span class="faq-block-list__question" itemprop="name">What is AI in software development?</span> <button class="faq-icon" aria-hidden="true"></button></div><div class="faq-block-list__answer" itemscope="" itemprop="acceptedAnswer" itemtype="https://schema.org/Answer"> <span itemprop="text"><p>AI is used in software development to help write code faster and more effectively, automate manual tasks, and speed up the testing process. Using AI in software app development, one can expect the app to be more robust, speedy, and almost error-free.</p> </span></div> </li> <li class="faq-block-list__list-item" itemscope="" itemprop="mainEntity" itemtype="https://schema.org/Question"><div class="faq-btn" id="faq-button-2" aria-expanded="false"> <span class="faq-block-list__question" itemprop="name">How much does an app with AI cost?</span> <button class="faq-icon" aria-hidden="true"></button></div><div class="faq-block-list__answer" itemscope="" itemprop="acceptedAnswer" itemtype="https://schema.org/Answer"> <span itemprop="text"><p>Custom AI apps may cost from $15 K up to $70-100K and more. The cost usually comes from complexity, functionality, and exclusiveness.</p> </span></div> </li> <li class="faq-block-list__list-item" itemscope="" itemprop="mainEntity" itemtype="https://schema.org/Question"><div class="faq-btn" id="faq-button-3" aria-expanded="false"> <span class="faq-block-list__question" itemprop="name">What is an AI development company?</span> <button class="faq-icon" aria-hidden="true"></button></div><div class="faq-block-list__answer" itemscope="" itemprop="acceptedAnswer" itemtype="https://schema.org/Answer"> <span itemprop="text"><p>An AI company is an AI technology vendor who has got broad expertise under their belt, an impressive project portfolio in various business domains. AI, data scientists, software engineers, quality assurance specialists can usually work on an average project.</p> </span></div> </li> <li class="faq-block-list__list-item" itemscope="" itemprop="mainEntity" itemtype="https://schema.org/Question"><div class="faq-btn" id="faq-button-4" aria-expanded="false"> <span class="faq-block-list__question" itemprop="name">What benefits AI provides business with?</span> <button class="faq-icon" aria-hidden="true"></button></div><div class="faq-block-list__answer" itemscope="" itemprop="acceptedAnswer" itemtype="https://schema.org/Answer"> <span itemprop="text"><p>The benefits are the following:</p><ul> <li>higher revenues</li> <li>reduced costs</li> <li>business process automation</li> <li>improved speed and accuracy</li> <li>simplified data management</li> <li>personalized customer experience</li> <li>business risks mitigation, etc.</li></ul> </span></div> </li>
'''

soup = BeautifulSoup(html, 'html.parser')

elems = soup.find_all("li", {"class": "faq-block-list__list-item"})

def get_QuesAns(elem):
    question = elem.find("span", {"class": "faq-block-list__question"}).text
    answer = elem.find("div", {"class": "faq-block-list__answer"}).find("p").text
    return {"question": question, "answer": answer}

print([get_QuesAns(elem) for elem in elems])

