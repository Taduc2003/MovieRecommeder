from django.test import TestCase
from ml.utils import get_data_loader
from surprise import SVD, accuracy


class DataLoaderTest(TestCase):
    def test_data_loader_row_count(self):
        data = [
            {"userId": 1, "movieId": 1, "rating": 4},
            {"userId": 2, "movieId": 2, "rating": 5},
        ]
        dataset = get_data_loader(data)
        df = dataset.df
        self.assertEqual(len(df), 2)

    # def test_data_loader_with_null(self):
    #     data = [
    #         {"userId": 1, "movieId": 1, "rating": 4},
    #         {"userId": None, "movieId": 2, "rating": 5},  # userId bị null
    #     ]
    #     dataset = get_data_loader(data)
    #     df = dataset.df
    #     # Chỉ còn 1 dòng hợp lệ
    #     self.assertEqual(len(df), 1)


class ModelQualityTest(TestCase):
    def test_rmse_threshold(self):
        data = [
            {"userId": 1, "movieId": 1, "rating": 4},
            {"userId": 1, "movieId": 2, "rating": 5},
            {"userId": 2, "movieId": 1, "rating": 3},
            {"userId": 2, "movieId": 2, "rating": 4},
        ]
        dataset = get_data_loader(data)
        trainset = dataset.build_full_trainset()
        model = SVD(n_epochs=5)
        model.fit(trainset)
        predictions = model.test(trainset.build_testset())
        rmse = accuracy.rmse(predictions, verbose=False)
        self.assertLess(rmse, 1.0)

    def test_predict_output_range(self):
        data = [
            {"userId": 1, "movieId": 1, "rating": 4},
            {"userId": 2, "movieId": 2, "rating": 5},
        ]
        dataset = get_data_loader(data)
        trainset = dataset.build_full_trainset()
        model = SVD(n_epochs=2)
        model.fit(trainset)
        pred = model.predict(uid=1, iid=1)
        self.assertTrue(1.0 <= pred.est <= 5.0)
