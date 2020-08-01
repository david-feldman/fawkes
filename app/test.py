from fawkes.protection import Fawkes

file_ra = ['/home/ubuntu/fawkes/app/tmp/1234']
fawkes_mode = 'mid'
protector = Fawkes("high_extract", "0", 1)
protector.run_protection(file_ra, mode=fawkes_mode, th=0.01, sd=1e9, lr=2, max_step=1000, batch_size=1, format="png", separate_target=True, debug=False)
