from mrjob.job import MRjob
from mrjob.step import MRStep

class RatingsBreakdown(MRjob):
    def steps(self):
        return [
            MRStep(mapper = '',
                reducer = '')
        ]

    def mapper_get_ratings(self, _, line):
        (userID, movieID, rating, timestamp) = line.split('\t')
        yield rating, 1

    def reducer_count_rating(self, key, values):
        yield key, sum(values)


if __name__ = '__main__':
    RatingsBreakdown.run()