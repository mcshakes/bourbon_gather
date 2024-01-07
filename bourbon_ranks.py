from scraper import bourbon_culture
from services.rds_client import RDSClient
import boto3

def create_boto_session():
    return boto3.Session(TEST, OTHER_STUFF)

def check_rds_instance():
    session = create_boto_session()
    rds_client = RDSClient(session, RDS_ZONE)
    status = rds_client.return_rds_status(DB_NAME)

def main():
    # bourbon_culture.run_scraper()    
    # check_rds_instance()    
    db.refresh()

if __name__ == "__main__":
    main()
