import subprocess # allows to execute scripts
# script to execute the data fetching and processing of data to industry_crypto_returns.csv

def run_script(script_path): # defining this just to make main() cleaner
    print(f'Running: {script_path}')

    subprocess.run(["python", script_path], check=True)
    print(f"Finished: {script_path}")
    
def main():
    run_script('fetch_data_ken-french.py')
    run_script('fetch_data_yfinance.py')
    run_script('process_data.py')

if __name__ == "__main__":
    main() # check if scripts is being run directly, if so calls main() function.

