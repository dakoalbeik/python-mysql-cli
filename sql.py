insertApartment =  (
    "INSERT INTO apartments "
    "(building_number, apartment_number, " 
    "apartment_view, is_occupied, "
    "square_footage, room_count, "
    "bathroom_count, is_furnished) "
    "VALUES (%(building_number)s, %(apartment_number)s, %(apartment_view)s, %(is_occupied)s, %(square_footage)s, %(room_count)s, %(bathroom_count)s, %(is_furnished)s)"
)

insertApplicant = (
    "INSERT INTO applicants "
	"(name, social_security, income, email, phone_number, contact_date) "
    "VALUES (%(name)s, %(social_security)s, %(income)s, %(email)s, %(phone_number)s, %(contact_date)s)"
)

insertApplication = (
    "INSERT INTO applications "
    "(screening_result, application_date, applicant_id) " 
    "VALUES (%(screening_result)s, %(application_date)s, %(applicant_id)s)"
)

insertResident = (
    "INSERT INTO residents "
    "(apartment_id, applicant_id) " 
    "VALUES (%(apartment_id)s, %(applicant_id)s)"
)

insertMaintenenceOrder = (
    "INSERT INTO maintenence_orders "
    "(details, order_status, submission_date, completion_date, resident_id) "
    "VALUES (%(details)s, %(order_status)s, %(submission_date)s, %(completion_date)s, %(resident_id)s)"
)

insertPet = (
    "INSERT INTO pets "
    "(name, weight, pet_type, color, is_service_animal, age, resident_id) "
    "VALUES (%(name)s, %(weight)s, %(pet_type)s, %(color)s, %(is_service_animal)s, %(age)s, %(resident_id)s)"
)

