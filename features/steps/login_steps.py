from behave import given, when, then
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@given ('user membuka halaman Login orangeHRM')
def step_membukaHalamanLogin(context):
    context.login_page = LoginPage(context.driver) #dipanggil dulu atasnya
    context.login_page.openURL() # baru di panggil method nya

@when ('user memasukkan username "{username}"')
def step_inputusername(context, username):
    context.login_page = LoginPage(context.driver)
    context.login_page.input_username(username)

@when ('user memasukkan password "{password}"')
def step_inputpassword(context, password):
    context.login_page = LoginPage(context.driver)
    context.login_page.input_password(password)

@when ('user menekan tombol login')
def step_clicktombollogin(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.click_login_button()

@then ('user berhasil login dan masuk ke halaman dashboard')
def step_berhasilLogin(context):
    dashboard_page = DashboardPage(context.driver)
    assert dashboard_page.memastikantulisan_dashboard(), \
        " Dashboard tidak ditampilkan setelah login"
    

#Negative case
@then ('pesan "{message}" ditampilkan') # ekspektasilogineror
def step_gagalloginpesaneror(context, message):
    actual_pesan = context.login_page.pesan_eror()

    assert actual_pesan == message,\
    f'Expected: "{message}", Actual : "{actual_pesan}"'

@when ('user tidak mengisi username')
def step_usertidakinputusername(context):
    pass

@when ('user tidak mengisi password')
def step_usertidakinputpassword(context):
    pass

@then('pesan "{message}" ditampilkan pada field Username')#ekspektasi tidak input username "Required"
def step_then(context, message):
    pesan_asli = context.login_page.erorinput_username()

    assert pesan_asli == message,\
    f'Expected: "{message}", Actual : "{pesan_asli}"'
   

@then ('pesan "{message}" ditampilkan pada field Password') #ekspektasi tidak input password "Required"
def step_tidak_input_password(context, message):
    pesan_asli = context.login_page.erorinput_password()

    assert pesan_asli == message, \
    f'Expected: "{message}", Actual : "{pesan_asli}"'

    




