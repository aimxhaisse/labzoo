# LabZoo's Design Notes

We have the following commands:

* `labzoo-run`
* `labzoo-process`
* `labzoo-report`

## LabZoo Run

Runs one or several checks on one or several targets.

Input parameters:

* YAML file describing the checks to perform
* Path to a SQLite3 database (existing, or not)

## LabZoo Process

Generates Result from the RawOutput.

Input parameters:

* YAML file describing how to generate the report
* Path to a SQLite3 database (existing)

## LabZoo Report

Offers an HTTP web interface to visualize the content of a database.

Input parameters:

* YAML file describing how to generate the report
* Path to a SQLite3 database (existing)
* HTTP interface to use

## LabZoo YAML config file

```
name: kernel performance
description: a serie of benchmarks that check the performances on kernels
targets:
    - mxs-benchmark-node-performance.ocs.online.net
checks:
    - name: NBD latency
      description: checks the I/O latency of a mounted NBD device
      type: IOPingRamFS
    - name: IPerf local
      description: checks the local network performances
      type: IPerfLocal
    - name: Stress wget
      description: checks the network and I/O performances
      type: StressWget
      params:
        - parallel_runs: 1
	  duration: 10
        - parallel_runs: 4
	  duration: 60
	- parallel_runs: 16
	  duration: 60
report:
    group-by:
        - env.kernel
	- params.Stress wget.parallel_runs
```

## LabZoo Database Model

* Session
* Check (Machine, Parameters, RawOutput)
* Machine (IP, Hostname, Environment)
* Environment (Kernel, Hostname, ...)
* RawOutput
* Result (id, generated_at)
* ResultValue (name, value, metric)
* ResultPoints (name, values, metric)
