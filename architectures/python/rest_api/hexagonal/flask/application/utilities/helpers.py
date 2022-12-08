import logging
import traceback

from datetime import datetime, date
from flask.json import JSONEncoder
from google.cloud.firestore import GeoPoint
from google.api_core.datetime_helpers import DatetimeWithNanoseconds
from itertools import islice
from urllib import parse


def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


class JsonEncoder(JSONEncoder):
    def default(self, obj):
        # https://github.com/googleapis/google-cloud-python/blob/master/api_core/google/api_core/datetime_helpers.py
        # if isinstance(obj, DatetimeWithNanoseconds):
        # return obj.rfc3339()
        if isinstance(obj, (datetime, date, DatetimeWithNanoseconds)):
            return obj.isoformat()
        if isinstance(obj, GeoPoint):
            return {"lat": obj.latitude, "lon": obj.longitude}
        # raise TypeError("Type %s not serializable" % type(obj))
        return JSONEncoder.default(self, obj)


def collection_stream_keys(collection, keys, id_=True):

    data = []
    for doc in collection.stream():
        try:
            dict_doc = {k: v for k, v in doc.to_dict().items() if k in (keys)}
            if id_:
                dict_doc.update({"uid": doc.id})
                data.append(dict_doc)
            else:
                data.append(dict_doc)
        except KeyError as e:
            logging.error((KeyError, e))
            data.append(dict_doc)
            continue
        except Exception as e:
            logging.error(traceback.format_exc())

    return data
