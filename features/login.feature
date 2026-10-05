Feature: Login OrangeHRM

@positive
Scenario: login dengan username dan password yang valid
    Given user membuka halaman Login orangeHRM
    When user memasukkan username "Admin" 
    And user memasukkan password "admin123"
    And user menekan tombol login
    Then user berhasil login dan masuk ke halaman dashboard


@negative @invalid_username
Scenario: login menggunakan username tidak valid
    Given user membuka halaman Login orangeHRM
    When user memasukkan username "InvalidUser"
    And user memasukkan password "admin123"
    And user menekan tombol login
    Then pesan "Invalid credentials" ditampilkan

@negative 
Scenario: Login menggunakan password tidak valid
    Given user membuka halaman Login orangeHRM
    When user memasukkan username "Admin"
    And user memasukkan password "wrongpassword"
    And user menekan tombol login
    Then pesan "Invalid credentials" ditampilkan

@negative @invalid_input
Scenario: Login tanpa mengisi username
    Given user membuka halaman Login orangeHRM
    When user tidak mengisi username
    And user memasukkan password "admin123"
    And user menekan tombol login
    Then pesan "Required" ditampilkan pada field Username

@negative @invalid_input
Scenario: Login tanpa mengisi password
    Given user membuka halaman Login orangeHRM
    When user memasukkan username "Admin"
    And user tidak mengisi password
    And user menekan tombol login
    Then pesan "Required" ditampilkan pada field Password


