
<p>    
<a href="https://github.com/wizkiye/pyethiojobs.git">    
<img src="./.github/images/logo.png" alt="PyEthioJobs">    
</a>    
<br>    
<b>Asynchronous <a href="https://ethiojobs.net">ethiojobs</a> Scraper written with python3 </b>    
<br>    
<a href="">    
Examples</a>    

# What is this?

Asynchronous python3 Scrapper for ethiojobs.net

# Installation

`pip3 install -U git+https://github.com/wizkiye/pyethiojobs.git`

# Example Usage



```python 
from pyethiojobs import EthioJobs  
from pyethiojobs.types import EmploymentType

ethiojobs = EthioJobs()


#Searching for jobs
async def main():  
    results = await ethiojobs.search(
        "designer", 
        limit=10, 
        employment_type=EmploymentType.FULL_TIME
    )  # this will return list of jobs 
    for result in results:
        print(result.title) 
        print(result.link) 

# Getting list of categories        
async def main():  
    categories = await ethiojobs.get_categories()
    for category in categories:
        print(category.name)
        print(category.link)
        await category.get_jobs()  # this will return list of jobs in the category
    

# Getting list of jobs in a category
async def main():  
    jobs = await ethiojobs.get_category("category_link or Category Object")
    for job in jobs:
        print(job.title)
        print(job.link)

# Getting the latest jobs
async def main():  
    jobs = await ethiojobs.get_latest_jobs()
    for job in jobs:
        print(job.title)
        print(job.link)
        
# Getting Government jobs
async def main():  
    jobs = await ethiojobs.get_gov_jobs() # this will return list of GovJob
    for job in jobs:
        print(job.company)
        print(job.link)
if __name__ == "__main__":  
    import asyncio     
    loop = asyncio.get_event_loop()  
    loop.run_until_complete(main())
```  

# Using Decorators

```python
from pyethiojobs import EthioJobs, filters
from pyethiojobs.types import  Job
ethiojobs = EthioJobs()

@ethiojobs.on_new_jobs()
async def new_job_handler(job: Job):
      print(job.__dict__)
     
     
# this is not tested yet :D
@ethiojobs.on_new_jobs(
    filters.valid_through(20) 
    & filters.work_place("Addis Ababa") 
    & ~filters.hiring_organization("Ethio Telecom")
)
async def new_filtered_job_handler(job: Job):
      print(job.__dict__)

if __name__ == '__main__':
     ethiojobs.run(poll_interval=30)
```

# Contributing

If you want to contribute to this project, please read the [CONTRIBUTING.md](CONTRIBUTING.md) file.

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

# Acknowledgments

* [ethiojobs](https://ethiojobs.net) for providing the data




