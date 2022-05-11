from datetime import datetime

import pytest

from ORM.data_access_layer import DataAccessLayer


@pytest.fixture
def database_with_setup():
    obj_data_access_layer = DataAccessLayer()
    obj_data_access_layer.initialize_database("sqlite:///:memory:")
    obj_data_access_layer.prep_db()

    return obj_data_access_layer


def test_getting_probes(database_with_setup):
    results = database_with_setup.get_all_probes(
        DataAccessLayer.Displayed_Parameter_Probe
    )

    assert len(results) == 5


def test_getting_last_inserted_probe(database_with_setup):
    probe = DataAccessLayer.Displayed_Parameter_Probe(
        time=datetime(2021, 6, 7, 8, 17, 44, 988117),
        current_L1="last_inserted",
    )

    database_with_setup.insert_probe(probe)

    expected_result = DataAccessLayer.Displayed_Parameter_Probe(
        time=datetime(2021, 6, 7, 8, 17, 44, 988117),
        current_L1="last_inserted",
    )

    result = database_with_setup.get_last_probe(
        DataAccessLayer.Displayed_Parameter_Probe
    )

    assert result == expected_result


def test_getting_probes_in_relationship(database_with_setup):
    probe = DataAccessLayer.Displayed_Parameter_Probe(
        line_voltage_L1=str(-1.916676736030763e234),
        line_voltage_L2=323,
        line_voltage_L3=321,
        time=datetime(2021, 6, 7, 8, 17, 44, 988223),
    )

    database_with_setup.insert_probe(probe)

    results = database_with_setup.get_all_device_setting_entity()

    assert len(results) == 2

    assert results[0].device_setting_name == "first_device_entity_tested_name"

    assert len(results[0].displayed_parameter_probes) == 3


def test_getting_settings_entity_probes_date_range(database_with_setup):
    device_entitties = database_with_setup.get_all_device_setting_entity()

    device_entity_id = device_entitties[0].Id

    (
        min_date_time,
        max_date_time,
    ) = database_with_setup.get_device_settings_entity_probes_date_range(
        device_entity_id
    )

    assert min_date_time == datetime(2021, 9, 11, 9, 45, 1)
    assert max_date_time == datetime(2021, 9, 11, 9, 46, 55)


def test_filtering_probes_with_dates_range_with_one_ORM_function(database_with_setup):
    device_entitties = database_with_setup.get_all_device_setting_entity()
    device_entity_id = device_entitties[0].Id

    datetime_range_min = datetime(2021, 9, 11, 9, 45, 2)
    datetime_range_max = datetime(2021, 9, 11, 9, 46, 54)

    probes = database_with_setup.get_filtered_device_setting_entity_by_id_with_datetime_filtered_with_one_ORM_object(
        device_entity_id, datetime_range_min, datetime_range_max
    ).displayed_parameter_probes

    assert len(probes) == 1

    datetime_range_min = datetime(2021, 9, 11, 9, 45, 1)
    datetime_range_max = datetime(2021, 9, 11, 9, 46, 54)

    probes = database_with_setup.get_filtered_device_setting_entity_by_id_with_datetime_filtered_with_one_ORM_object(
        device_entity_id, datetime_range_min, datetime_range_max
    ).displayed_parameter_probes

    assert len(probes) == 2

    datetime_range_min = datetime(2021, 9, 11, 9, 45, 2)
    datetime_range_max = datetime(2021, 9, 11, 9, 46, 55)

    probes = database_with_setup.get_filtered_device_setting_entity_by_id_with_datetime_filtered_with_one_ORM_object(
        device_entity_id, datetime_range_min, datetime_range_max
    ).displayed_parameter_probes

    assert len(probes) == 2

    datetime_range_min = datetime(2021, 9, 11, 9, 45, 1)
    datetime_range_max = datetime(2021, 9, 11, 9, 46, 55)

    probes = database_with_setup.get_filtered_device_setting_entity_by_id_with_datetime_filtered_with_one_ORM_object(
        device_entity_id, datetime_range_min, datetime_range_max
    ).displayed_parameter_probes

    assert len(probes) == 3


def test_getting_phase_voltage_element_from_device_entity_from_filtered_option(
    database_with_setup,
):
    device_entitties = database_with_setup.get_all_device_setting_entity()
    device_entity_id = device_entitties[0].Id

    datetime_range_min = datetime(2021, 9, 11, 9, 45, 1)
    datetime_range_max = datetime(2021, 9, 11, 9, 46, 55)

    probes = database_with_setup.get_filtered_device_setting_entity_by_id_with_datetime_filtered_with_one_ORM_object(
        device_entity_id, datetime_range_min, datetime_range_max
    ).displayed_parameter_probes

    phase_voltage_element = probes[0].phase_voltage_datas

    assert len(probes) == 3

    assert phase_voltage_element.phase_voltage_L1 == "34"
    assert phase_voltage_element.phase_voltage_L2 == "346"
    assert phase_voltage_element.phase_voltage_L3 == "543"


def test_getting_phase_voltage_element_from_device_entity(database_with_setup):
    device_entitties = database_with_setup.get_all_device_setting_entity()
    device_entitties[0].Id

    device_setting_entity = device_entitties[0]

    probes = device_setting_entity.displayed_parameter_probes

    phase_voltage_element = probes[0].phase_voltage_datas

    assert len(probes) == 3

    assert phase_voltage_element.phase_voltage_L1 == "34"
    assert phase_voltage_element.phase_voltage_L2 == "346"
    assert phase_voltage_element.phase_voltage_L3 == "543"
