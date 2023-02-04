from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from nuget import get_nuget_packages
from nuget import PACKAGE_URL

class NuGetExtension(Extension):
    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        query = event.get_argument() or str()
        take = int(extension.preferences['take'])

        nuget_packages = get_nuget_packages(query, take)

        items = []

        for package in nuget_packages:
            items.append(ExtensionResultItem(icon="images/icon.png",
                                             name=package.title,
                                             description=package.description,
                                             on_enter=OpenUrlAction(PACKAGE_URL + package.id)))

        return RenderResultListAction(items)


if __name__ == '__main__':
    NuGetExtension().run()
