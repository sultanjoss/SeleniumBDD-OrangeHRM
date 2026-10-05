Feature: Pencarian employee pada menu PIM

  Background:
    Given user membuka halaman Login orangeHRM
    When user memasukkan username "Admin"
    And user memasukkan password "admin123"
    And user menekan tombol login
    Then user berhasil login dan masuk ke halaman dashboard

  @search_employee
  Scenario Outline: mencari informasi employee menggunakan seluruh filter employee informasi
    Given user membuka menu PIM
    When user mengisi nama employee "<employee_name>"
    And user mengisi id employee "<employee_id>"
    And user memilih status employee "<employee_status>"
    And user memilih include "<include>"
    And user mengisi nama supervisor "<supervisor_name>"
    And user memilih job title "<job_title>"
    And user memilih sub unit "<sub_unit>"
    And user menekan tombol search pada informasi employee
    Then hasil pencarian akan ditampilkan di tabel bawah

    Examples:
      | employee_name      | employee_id | employee_status     | include                | supervisor_name | job_title        | sub_unit          |
      | Peter Mac Anderson |        0123 | Full-Time Permanent | Current Employees Only | Ranga  Akunuri  | Automaton Tester | Quality Assurance |

  @add_employee
  Scenario Outline: Menambahkan employee Baru
    Given user membuka menu PIM
    When user click tombol add
    Then user berada di halaman add employee
    When user mengisi field first name "<first_name>"
    And user mengisi field middle name "<middle_name>"
    And user mengisi field last name "<last_name>"
    And user mengisi field employee id "<pekerja_id>"
    And user memasukkan foto profile "<foto>"
    And user click tombol save pada add employee
    Then user berhasil melakukan add employee berpindah kehalaman personal details

    Examples:
      | first_name | middle_name | last_name | pekerja_id | foto                   |
      | fahmis     | ucup2       | jago      |     987212 | test_data/profil01.png |
      | anun       | ucup2       | jago      |      98212 | test_data/profil01.png |
