-- 01 Mountain Peaks

CREATE TABLE IF NOT EXISTS mountains(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS peaks(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    mountain_id INT,
    CONSTRAINT fk_peaks_mountains
        FOREIGN KEY (mountain_id)
            REFERENCES mountains(id)
);

-- 02. Trip Organization

SELECT
    d.id AS driver_id,
    v.vehicle_type as vehicle_type,
    CONCAT(d.first_name, ' ', d.last_name) AS driver_name
FROM
    campers AS d
JOIN vehicles AS v ON v.driver_id = d.id;

-- 03. SoftUni Hiking

SELECT
    r.start_point,
    r.end_point,
    c.id AS leader_id,
    CONCAT(c.first_name, ' ', c.last_name) AS leader_name
from routes AS r
JOIN
    campers AS c ON c.id = r.leader_id;

-- 04. Delete Mountains

CREATE TABLE mountains(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE peaks(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    mountain_id INT,
    CONSTRAINT fk_mountain_id
                  FOREIGN KEY (mountain_id)
                  REFERENCES mountains(id) ON DELETE CASCADE
);

-- 05 Create table relations based on graph **

CREATE TABLE clients(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE projects(
    id SERIAL PRIMARY KEY,
    client_id INT,
    project_lead_id INT,
    CONSTRAINT fk_client_id_clients
                     FOREIGN KEY (client_id)
                     REFERENCES clients(id)
);

CREATE TABLE employees(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    project_id INT,
    CONSTRAINT fk_project_id_projects
                      FOREIGN KEY (project_id)
                      REFERENCES projects(id)
);

ALTER TABLE projects
ADD CONSTRAINT fk_project_lead_id_employee_id
    FOREIGN KEY (project_lead_id)
    REFERENCES employees(id);

