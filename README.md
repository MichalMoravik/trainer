# Trainer ⏱

Lightweight benchmarking package with zero dependencies

## Usage

```Python
t = Trainer().round(2)

with t('metric1'):
    time.sleep(0.5)

with t('metric2'):
    time.sleep(0.3)

m = t.add_total('total').metrics
print(m)
```

**output:**

```
{
    'metric1': {'start': 1656844808.09, 'end': 1656844808.59, 'interval': 0.5},
    'metric2': {'start': 1656844808.59, 'end': 1656844808.89, 'interval': 0.3},
    'total': {'start': 1656844808.09, 'end': 1656844808.89, 'interval': 0.8}
}
```

> for more examples, see folder [examples](examples/example.py)

## Features

### Contexts

- using Python [contexts](https://docs.python.org/3/library/contextlib.html),
you can indent specific parts of the code you want to benchmark
- each measured code part produces a 'metric' dictionary with name (key),
start (epoch), end (epoch), interval (epoch)
- all metrics can be retrieved at any point by calling `trainer.metrics`

### Total Execution Time

- you can add the total execution time by executing `trainer.add_total()`
at the end
- by default, the total time considers the first metric's start time as its
start, but it is possible to prematurely start measurement by calling
`trainer.start_measuring()` instead

### Rounding

- all epoch timestamps can be rounded to any number of decimals using
`trainer.round(<int>)`
- all epoch timestamps can be rounded to full seconds (making them
integers instead of floats) by executing `trainer.round()` or `trainer.round(0)`

</br>

[go to examples](examples/example.py)
