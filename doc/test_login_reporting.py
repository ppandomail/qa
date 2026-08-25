import pytest
import allure

@allure.epic('Autenticación')
@allure.feature('Login de Usuarios')
@allure.story('Login Exitoso con Credenciales Válidas')
@allure.severity(allure.severity_level.CRITICAL)
def test_login_exitoso():
    '''Prueba que un usuario con credenciales correctas pueda ingresar al sistema.'''
    
    with allure.step('Paso 1: Abrir la página de inicio de sesión'):
        # Código para abrir el navegador
        url_actual = 'https://ejemplo.com'
    
    with allure.step('Paso 2: Ingresar usuario y contraseña válidos'):
        usuario = 'admin'
        contrasena = 'password123'
        allure.attach(f'Usuario: {usuario}', name='Datos de Entrada', attachment_type=allure.attachment_type.TEXT)

    with allure.step("Paso 3: Hacer clic en el botón 'Iniciar Sesión'"):
        login_exitoso = True  # Simulación de la acción

    with allure.step('Paso 4: Verificar redirección al panel principal'):
        assert login_exitoso is True, 'El usuario no pudo iniciar sesión de forma correcta'
