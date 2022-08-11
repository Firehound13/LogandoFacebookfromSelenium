from time import sleep
import getpass
from selenium import webdriver
from webdriver.manager.chrome import ChromeDriverManager
from config import URL

usuario_facebook = input("Digite seu email de acesso ao facebook: ")
senha = getpass.getpass("Digite a senha: ")

driver= webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)
print("- Abrindo o facebook ")
sleep(1)

campo_usuario = driver.find_element_by_id('email')
campo_usuario.send_keys(usuario_facebook)
print("Inserindo usuário no campo email: ")

campo_senha = driver.find_element_by_id('pass')
campo_senha.send_keys(senha)
print("Inserindo senha:")

botao_login = driver.find_element_by_id('loginbutton')
botao_login.click()
print("Completando o acesso!")
input("Aperte qualquer tecla para sair.")
driver.quit()
print("- Finalizado.")
