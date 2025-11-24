from CustomerBuilder import WebBuilder, MobileBuilder, create_mobile_customer

def main():
    web_builder = WebBuilder()
    web_customer = (web_builder
        .firstName("John")
        .lastName("Doe")
        .middleName("A.")
        .primaryEmail("johndoe@gmail.com")
        .secondaryEmail("john2doe@gmail.com")
        .primaryPhoneNumber("123-456-7890")
        .secondaryPhoneNumber("098-765-4321")
        .build())
    print("Web Customer:", web_customer)

    mobile_builder = MobileBuilder()
    mobile_customer = (mobile_builder
        .firstName("Jane")
        .lastName("Smith")
        .primaryEmail("janes@gmail.com")
        .primaryPhoneNumber("555-555-5555")
        .build())
    print("Mobile Customer:", mobile_customer)

    try:
        # Missing last name
        invalid_web_customer = (WebBuilder()
            .firstName("Invalid")
            .primaryEmail("email")
            .primaryPhoneNumber("000-000-0000")
            .build())
    except ValueError as e:
        print("Error building web customer:", e)

    web_customer2 = ("Alice", "Wonderland", "aw@gmail.com", "111-222-3333")
    print("Web Customer 2:", web_customer2)

if __name__ == "__main__":
    main()