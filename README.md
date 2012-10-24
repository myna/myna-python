# Python Client for Myna

A simple Python client for Myna.

This client uses the built-in `httplib` to allow you to suggest and reward your Myna clients. It has no external dependencies. Tested in Python 2.7.

## Installation and Usage

Just copy `myna.py` somewhere that is accessible from your code. Then to create an experiment:

```python
expt = Experiment('45923780-80ed-47c6-aa46-15e2ae7a0e8c')
```

Get a suggestion:

```python
suggestion = expt.suggest()
```

Do something with the choice Myna has made:

```python
doSomething(suggestion.choice)
```

Finally, reward the suggestion if the user did what you hoped they would.

```python
suggestion.reward()
```

See the API reference below for complete details.

## TODO

Better handle errors that aren't in the Myna format.

## Development

Run the tests with

```bash
python -m unittest test
```

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

Represents a suggestion returned by an experiment.

#### Suggestion.choice

The choice associated with this suggestion. A string.

#### Suggestion.token

The token associated with this suggestion. A string.

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
