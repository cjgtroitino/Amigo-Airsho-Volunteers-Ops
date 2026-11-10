CREATE TABLE volunteers (
    volunteer_id VARCHAR(36) PRIMARY KEY,
    org_id VARCHAR(36),
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    waiver_signed BOOLEAN DEFAULT FALSE,
    waiver_timestamp TIMESTAMP NULL,
    assigned_committee VARCHAR(50),
    shift_date DATE NOT NULL,
    shift_start TIME NOT NULL,
    shift_end TIME NOT NULL,
    base_pass_status VARCHAR(20) DEFAULT 'PENDING',
    flightline_driver_certified BOOLEAN DEFAULT FALSE,
    check_in_status BOOLEAN DEFAULT FALSE,
    check_in_timestamp TIMESTAMP NULL
);
