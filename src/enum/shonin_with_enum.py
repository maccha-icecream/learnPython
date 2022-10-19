import dataclasses
import sys, enum

# 申請ステータス
class ShinseiStatus(enum.Enum):
    # 審査中
    IN_INSPECTION = enum.auto()
    # 差し戻し中
    SEND_BACK = enum.auto()
    # 承認済み
    APPROVALED = enum.auto()
    # 実施中
    IN_PROGRESS = enum.auto()
    # 中断中
    IN_SUSPENDED = enum.auto()
    # 終了
    DONE = enum.auto()

@dataclasses.dataclass
class ShinseiStatusTransition:
    __allowed : {}
    def __init__(self) -> None:
        self.__allowed = {
            ShinseiStatus.IN_INSPECTION: {
                ShinseiStatus.SEND_BACK,
                ShinseiStatus.APPROVALED
            },
            ShinseiStatus.SEND_BACK: {
                ShinseiStatus.IN_INSPECTION,
                ShinseiStatus.DONE
            },
            ShinseiStatus.APPROVALED: {
                ShinseiStatus.IN_PROGRESS,
                ShinseiStatus.DONE
            },
            ShinseiStatus.IN_PROGRESS: {
                ShinseiStatus.DONE,
                ShinseiStatus.IN_SUSPENDED
            },
            ShinseiStatus.IN_SUSPENDED: {
                ShinseiStatus.IN_PROGRESS,
                ShinseiStatus.DONE
            }
        }

    def can_transit(self, _from:ShinseiStatus, _to:ShinseiStatus) -> bool:
        allowed_status = self.__allowed[_from]
        return _to in allowed_status

if __name__ == "__main__":
    shinsei_status_transition = ShinseiStatusTransition()
    assert shinsei_status_transition.can_transit(ShinseiStatus.APPROVALED, ShinseiStatus.SEND_BACK)
    assert shinsei_status_transition.can_transit(ShinseiStatus.IN_INSPECTION, ShinseiStatus.APPROVALED)