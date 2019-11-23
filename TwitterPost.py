from selenium import webdriver

## Variaveis

MY_USER_NAME = 'seu usuario'
MY_PASSWORD = 'sua senha aqui'

## Acessando o Twitter

driver = webdriver.Chrome()
driver.get('http://twitter.com/login')

## Preenchendo o USUARIO

name = driver.find_element_by_xpath("//input[@class='js-username-field email-input js-initial-focus']")
name.send_keys(MY_USER_NAME)

## Preenchendo a SENHA

senha = driver.find_element_by_xpath("//input[@class='js-password-field']")
senha.send_keys(MY_PASSWORD)
name.submit()

## Acessando pag de POST

driver.get('https://twitter.com/intent/tweet?text=')

## Escrevendo a Mensagem

MY_MSG = 'POST PYTHON'
text = driver.find_element_by_xpath("//textarea[@id='status']")
text.send_keys(MY_MSG)

## Clicando em TWEETAR

driver.find_element_by_xpath("//input[@value='Tweetar']").click()

