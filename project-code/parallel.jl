# first we create the channels of type {T} and size (int). 
julia> const jobs = Channel{Int}(32);
julia> const results = Channel{Tuple}(32);

julia> function do_work()
          for job_id in jobs
	      exec_time = rand()
	      sleep(exec_time)
	      put!(results, (job_id, exec_time))
	  end
	end;

julia> make_jobs(n)
          for i in 1:n
	      put!(jobs,i)
	  end
	end;

julia> n=12

julia> @async make_jobs(n)

julia> for i in 1:4
          @async do_work()
	end

julia> @elapsed while n > 0
          job_id, exec_time = take!(results)
	  println("$job_id finished in $(round(exec_time; digits=2)) seconds")
	  global n = n-1
	end
```
