from Util.Bases import ClassifierBase
from Util.Metas import SKCompatibleMeta

from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier


class SKAdaBoost(AdaBoostClassifier, ClassifierBase, metaclass=SKCompatibleMeta):
    pass


class SKRandomForest(RandomForestClassifier, ClassifierBase, metaclass=SKCompatibleMeta):
    pass
