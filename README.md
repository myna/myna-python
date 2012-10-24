# Python Client for Myna

A simple Python client for Myna.

This client uses the built-in `httplib` to allow you to suggest and reward your Myna clients. It has no external dependencies. Tested in Python 2.7.

## Development

Run the tests with

```bash
python -m unittest test
```

## TODO

- Better error handling
- Documentation
- Tests
- Some kind of packaging?

## API Reference

### Experiment

Represents an experiment. Construct by passing in a string UUID.

```python
expt = Experiment('45923780-80ed-47c6-aa46-15e2ae7a0e8c')
```

#### Experiment.uuid

The UUID of this experiment. A string.

#### Experiment.suggest()

Retrieves a suggestion from the Myna server. Returns a `Suggestion` object on success. On error a `MynaError` exception is raised.


### Suggestion

#### Suggestion.choice

#### Suggestion.token

#### Suggestion.reward([amount])

Rewards this suggestion. The optional amount defaults to 1.0, and must be a number between 0.0 and 1.0.

Returns `True` on success. Otherwise raises an exception as follows:

- `MynaError` if the Myna server sent back a response containing a Problem (see the [Myna API documentation on error handling](https://mynaweb.com/help/api#error-handling))
- `IOError` if some other error occurred


### MynaError

An exception raised when the Myna server returns a Problem. See [the API documentation on error handling](https://mynaweb.com/help/api#error-handling) for a description.

#### MynaError.code

A numeric code identifying the error.

#### MynaError.messages

Helpful messages associated with the error.
