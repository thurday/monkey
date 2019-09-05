import logging

from cc.services.reporting.report_exporter_manager import ReportExporterManager
from cc.services.reporting.aws_exporter import AWSExporter
from monkey_island.cc.services.remote_run_aws import RemoteRunAwsService
from monkey_island.cc.environment.environment import env
logger = logging.getLogger(__name__)


def populate_exporter_list():
    manager = ReportExporterManager()
    RemoteRunAwsService.init()
    if RemoteRunAwsService.is_running_on_aws() and ('aws' == env.get_deployment()):
        manager.add_exporter_to_list(AWSExporter)

    if len(manager.get_exporters_list()) != 0:
        logger.debug(
            "Populated exporters list with the following exporters: {0}".format(str(manager.get_exporters_list())))

