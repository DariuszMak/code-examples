import os
import typing
from datetime import datetime
from operator import and_

import sqlalchemy as sa
from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    and_,
    create_engine,
    func,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import contains_eager, relationship, sessionmaker


class DataAccessLayer:
    Base = declarative_base()

    def __init__(self):
        self.connection = None
        self.engine = None
        self.Session = None
        self.conn_string = None

        self.metadata = self.Base.metadata

        self.local_settings = None

        self.session = None

    class Device_Setting_Entity(Base):
        __tablename__ = "device_setting_entities"

        Id = Column(Integer, primary_key=True)
        time = Column(DateTime, default=datetime.now)

        device_id = Column(String(255))
        device_setting_name = Column(String(255))

        device_type = Column(Integer)

        settings_change_identifier = Column(String(255))

        displayed_parameter_probes = relationship(
            "Displayed_Parameter_Probe",
            order_by="asc(Displayed_Parameter_Probe.time)",
            back_populates="device_setting_entity",
        )

        def __repr__(self):
            return DataAccessLayer._repr(
                self,
                time=self.time,
                device_id=self.device_id,
                device_setting_name=self.device_setting_name,
                device_type=self.device_type,
                settings_change_identifier=self.settings_change_identifier,
            )

        def __eq__(self, other):
            if isinstance(other, DataAccessLayer.Device_Setting_Entity):
                return (
                    self.time == other.time
                    and self.device_id == other.device_id
                    and self.device_setting_name == other.device_setting_name
                    and self.device_type == other.device_type
                    and self.settings_change_identifier
                    == other.settings_change_identifier,
                )
            return False

    class Displayed_Parameter_Probe(Base):
        __tablename__ = "displayed_parameters_probes"

        Id = Column(Integer, primary_key=True)
        time = Column(DateTime, default=datetime.now)

        line_voltage_L1 = Column(String(255))
        line_voltage_L2 = Column(String(255))
        line_voltage_L3 = Column(String(255))

        device_setting_entity_Id = Column(
            Integer, ForeignKey("device_setting_entities.Id")
        )
        device_setting_entity = relationship(
            "Device_Setting_Entity", back_populates="displayed_parameter_probes"
        )

        phase_voltage_datas = relationship(
            "Phase_Voltage_Data",
            back_populates="displayed_parameter_probe",
            uselist=False,
        )

        def __repr__(self):
            return DataAccessLayer._repr(
                self,
                time=self.time,
                line_voltage_L1=self.line_voltage_L1,
                line_voltage_L2=self.line_voltage_L2,
                line_voltage_L3=self.line_voltage_L3,
            )

        def __eq__(self, other):
            if isinstance(other, DataAccessLayer.Displayed_Parameter_Probe):

                return (
                    self.time == other.time
                    and self.line_voltage_L1 == other.line_voltage_L1
                    and self.line_voltage_L2 == other.line_voltage_L2
                    and self.line_voltage_L3 == other.line_voltage_L3

                )

            return False

    class Phase_Voltage_Data(Base):
        __tablename__ = "phase_voltage_datas"

        Id = Column(Integer, primary_key=True)

        phase_voltage_L1 = Column(String(255))
        phase_voltage_L2 = Column(String(255))
        phase_voltage_L3 = Column(String(255))

        displayed_parameter_probe_Id = Column(
            Integer, ForeignKey("displayed_parameters_probes.Id")
        )
        displayed_parameter_probe = relationship(
            "Displayed_Parameter_Probe", back_populates="phase_voltage_datas"
        )

        def __repr__(self):
            return DataAccessLayer._repr(
                self,
                phase_voltage_L1=self.phase_voltage_L1,
                phase_voltage_L2=self.phase_voltage_L2,
                phase_voltage_L3=self.phase_voltage_L3,
            )

        def __eq__(self, other):
            if isinstance(other, DataAccessLayer.Phase_Voltage_Data):

                return (
                    self.phase_voltage_L1 == other.phase_voltage_L1
                    and self.phase_voltage_L2 == other.phase_voltage_L2
                    and self.phase_voltage_L3 == other.phase_voltage_L3
                )

    def displayed_paremeter_probe_all_columns(self):
        probe_test = self.Displayed_Parameter_Probe()
        probe_all_columns = probe_test.__mapper__.column_attrs.keys()

        # print(probe_test.__mapper__.attrs.keys())
        # print(probe_test.__mapper__.column_attrs.keys())

        for elem in probe_all_columns:
            # print(elem.name)
            probe_all_columns.remove(elem)

        return probe_all_columns

    def initialize_database(self, conn_string):
        self.engine = create_engine(conn_string, echo=False)
        self.metadata.create_all(self.engine)
        self.connection = self.engine.connect()
        self.Session = sessionmaker(bind=self.engine)
        self.session: sessionmaker = self.Session()

    def connect_database_with_filename(self, name):
        file_path = os.path.abspath(os.getcwd()) + "\\" + name
        self.initialize_database("sqlite:///" + file_path)

        # self.prep_db()

    def prep_db(self):
        first_device_setting_entity = DataAccessLayer.Device_Setting_Entity(
            device_id="98ff7089-1239-4bca-bf2f-c5b1c0c62d4d",
            device_setting_name="first_device_entity_tested_name",
        )

        second_device_setting_entity = DataAccessLayer.Device_Setting_Entity(
            device_id="d28928e5-d312-4f43-a95d-3891e9173ea9s",
            device_setting_name="second_device_entity_tested_name",
        )

        initial_probes_in_list = [
            DataAccessLayer.Displayed_Parameter_Probe(
                # Id = 2,
                time=datetime(2021, 9, 11, 9, 45, 1),
                line_voltage_L1="50",
                line_voltage_L2="100",
                line_voltage_L3="200",
                device_setting_entity=first_device_setting_entity,
            ),
            DataAccessLayer.Displayed_Parameter_Probe(
                # Id = 4,
                time=datetime(2021, 9, 11, 9, 45, 23),
                line_voltage_L1="1",
                line_voltage_L2="3",
                line_voltage_L3="4",
                device_setting_entity=first_device_setting_entity,
            ),
            DataAccessLayer.Displayed_Parameter_Probe(
                # Id = 2,
                time=datetime(2021, 9, 11, 9, 46, 55),
                current_L1="123",
                current_L2="342",
                current_L3="432",
                device_setting_entity=first_device_setting_entity,
            ),
            DataAccessLayer.Displayed_Parameter_Probe(
                # Id = 2,
                time=datetime(2021, 5, 19, 21, 39, 1),
                line_voltage_L1="33",
                line_voltage_L2="44",
                line_voltage_L3="55",
                device_setting_entity=second_device_setting_entity,
            ),
            DataAccessLayer.Displayed_Parameter_Probe(
                # Id = 4,
                time=datetime(2021, 5, 19, 21, 39, 20),
                line_voltage_L1="77",
                line_voltage_L2="88",
                line_voltage_L3="99",
                device_setting_entity=second_device_setting_entity,
            ),
        ]

        initial_phase_voltage_data = [
            DataAccessLayer.Phase_Voltage_Data(
                # Id = 2,
                phase_voltage_L1="34",
                phase_voltage_L2="346",
                phase_voltage_L3="543",
                displayed_parameter_probe=initial_probes_in_list[0],
            ),
            DataAccessLayer.Phase_Voltage_Data(
                # Id = 2,
                phase_voltage_L1="12",
                phase_voltage_L2="321",
                phase_voltage_L3="754",
                displayed_parameter_probe=initial_probes_in_list[3],
            ),
        ]

        with self.Session() as session:

            session.expire_on_commit = False

            with session.begin():
                try:
                    session.add_all(initial_phase_voltage_data)
                    session.commit()
                except:
                    session.rollback()
                    raise


    def insert_device_setting_entity(self, device_setting_entity):
        self.session.add(device_setting_entity)
        self.session.commit()

    def get_device_settings_entity_probes_date_range(self, device_setting_entity_id):
        result = (
            self.session.query(
                func.min(DataAccessLayer.Displayed_Parameter_Probe.time),
                func.max(DataAccessLayer.Displayed_Parameter_Probe.time),
            )
            .filter(
                DataAccessLayer.Displayed_Parameter_Probe.device_setting_entity_Id
                == device_setting_entity_id,
            )
            .one()
        )

        return result

    def get_filtered_device_setting_entity_by_id_with_datetime_filtered_with_one_ORM_object(
        self, device_setting_entity_id, datetime_from, datetime_to
    ):
        result = (
            self.session.query(DataAccessLayer.Device_Setting_Entity)
            .filter(
                DataAccessLayer.Device_Setting_Entity.Id == device_setting_entity_id
            )
            .outerjoin(
                DataAccessLayer.Displayed_Parameter_Probe,
                and_(
                    DataAccessLayer.Device_Setting_Entity.Id
                    == DataAccessLayer.Displayed_Parameter_Probe.device_setting_entity_Id,
                    DataAccessLayer.Displayed_Parameter_Probe.time.between(
                        datetime_from, datetime_to
                    ),
                ),
            )
            .options(
                contains_eager(
                    DataAccessLayer.Device_Setting_Entity.displayed_parameter_probes
                )
            )
            .populate_existing()
        ).one()

        return result

    def get_filtered_device_setting_entity_for_setting_change_identifier(self, device):
        result = (
            self.session.query(DataAccessLayer.Device_Setting_Entity)
            .filter(
                DataAccessLayer.Device_Setting_Entity.settings_change_identifier
                == device.settings_change_identifier,
            )
            .first()
        )
        return result

    def get_device_settings_entities_by_device_id(self, device_id):
        result = (
            self.session.query(DataAccessLayer.Device_Setting_Entity)
            .filter(DataAccessLayer.Device_Setting_Entity.device_id == device_id)
            .all()
        )
        return result

    def get_all_device_setting_entity(self):
        result = self.session.query(DataAccessLayer.Device_Setting_Entity).all()
        return result

    def insert_probe(self, probe):
        self.session.add(probe)
        self.session.commit()

    def get_all_probes(self, probe):
        result = self.session.query(probe).all()
        return result

    def get_last_probe(self, probe):
        result = self.session.query(probe).order_by(probe.Id.desc()).first()
        return result

    def _repr(obj, **fields: typing.Dict[str, typing.Any]):
        field_strings = []
        at_least_one_attached_attribute = False
        for key, field in fields.items():
            try:
                field_strings.append(f"{key}={field!r}")
            except sa.orm.exc.DetachedInstanceError:
                field_strings.append(f"{key}=DetachedInstanceError")
            else:
                at_least_one_attached_attribute = True
        if at_least_one_attached_attribute:
            return f"<{obj.__class__.__name__}({','.join(field_strings)})>"
        return f"<{obj.__class__.__name__} {id(obj)}>"

    def __del__(self):
        pass
