import argparse
import logging
from lease_analytics.utils.config_loader import load_config
from lease_analytics.utils.logging_config import setup_logging

def main():
    parser = argparse.ArgumentParser(description="Lease Analytics CLI")
    parser.add_argument("--import", dest="import_file", help="Import a CSV file into the database")
    parser.add_argument("--gui", action="store_true", help="Launch the NiceGUI dashboard")
    parser.add_argument("--summary", action="store_true", help="Show a summary of transactions")
    parser.add_argument("--export", nargs=2, metavar=("TABLE", "OUTPUT"), help="Export data to CSV")
    args = parser.parse_args()

    config = load_config()
    setup_logging(config.get("log_file"), config.get("log_level", "INFO"))
    log = logging.getLogger("lease_analytics")

    if args.import_file:
        from lease_analytics.core.importer import import_csv
        import_csv(args.import_file)
    elif args.gui:
        from lease_analytics.gui.dashboard import launch_gui
        launch_gui()
    elif args.summary:
        from lease_analytics.analytics.monthly_summary import show_summary
        show_summary()
    elif args.export:
        from lease_analytics.analytics.exports import export_table
        export_table(*args.export)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
