from behave import given, when, then
from pages.input_pim_pages import InputPIMpage
from pages.dashboard_page import DashboardPage
import time


@given ("user membuka menu PIM")
def user_menu_PIM(context):
    context.input_pim_pages = InputPIMpage(context.driver)

    context.input_pim_pages.open_pim_menu()
    assert context.input_pim_pages.employee_information_displayed(), \
    "Halaman Employee information tidak di tampilkan"

@when('user mengisi nama employee "{employee_name}"')
def step_input_employee_name(context, employee_name):
    context.input_pim_pages.input_employee_name(employee_name)

@when('user mengisi id employee "{employee_id}"')
def step_input_employee_id(context, employee_id):
    context.input_pim_pages.input_employee_id(employee_id)

@when('user memilih status employee "{employee_status}"')
def step_input_employee_status(context, employee_status):
    context.input_pim_pages.pilih_employee_status(employee_status)

@when('user memilih include "{include}"')
def step_input_inculude(context, include):
    context.input_pim_pages.pilih_include(include)

@when('user mengisi nama supervisor "{supervisor_name}"')
def step_input_nama_supervisor(context, supervisor_name):
    context.input_pim_pages.input_supervisor_name(supervisor_name)

@when('user memilih job title "{job_title}"')
def step_pilih_job_title(context, job_title):
    context.input_pim_pages.pilih_job_title(job_title)

@when('user memilih sub unit "{sub_unit}"')
def step_pilih_sub_unit(context, sub_unit):
    context.input_pim_pages.pilih_sub_unit(sub_unit)

@when('user menekan tombol search pada informasi employee')
def step_click_tombol_search(context):
    context.input_pim_pages.click_button_search()

@then('hasil pencarian akan ditampilkan di tabel bawah')
def step_hasil_pencarian_employee(context):
    assert context.input_pim_pages.get_record_found()

    time.sleep(3)






