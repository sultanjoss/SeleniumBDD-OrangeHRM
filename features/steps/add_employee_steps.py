from behave import given, when, then
from pages.input_pim_pages import InputPIMpage
from pages.dashboard_page import DashboardPage
import time


@when('user click tombol add')
def step_user_click_tombol_add(context):
    context.input_pim_pages.click_add_employee()

@then('user berada di halaman add employee')
def step_berada_dihalaman_addemployee(context):
    context.input_pim_pages.tampilan_add_employee()

@when('user mengisi field first name "{first_name}"')
def step_input_firstname(context, first_name):
    context.input_pim_pages.masukkan_first_name(first_name)

@when('user mengisi field middle name "{middle_name}"')
def step_input_middle_name(context, middle_name):
    context.input_pim_pages.masukkan_middle_name(middle_name)

@when('user mengisi field last name "{last_name}"')
def step_input_last_name(context, last_name):
    context.input_pim_pages.masukkan_last_name(last_name)

@when('user mengisi field employee id "{pekerja_id}"')
def step_input_pekerjaID(context, pekerja_id):
    context.input_pim_pages.masukkan_pekerja_ID(pekerja_id)


@when('user memasukkan foto profile "{foto}"')
def step_input_foto(context, foto):
    context.input_pim_pages.upload_profile_photo(foto)

@when('user click tombol save pada add employee')
def step_click_save_button(context):
    context.input_pim_pages.click_tombol_save()

@then('user berhasil melakukan add employee berpindah kehalaman personal details')
def step_berpindah_halaman_personaldetails(context):
    assert context.input_pim_pages.halaman_personal_details(), \
    " Halaman Personal Details tidak ditampilkan setelah employee disimpan "

    time.sleep(3)



